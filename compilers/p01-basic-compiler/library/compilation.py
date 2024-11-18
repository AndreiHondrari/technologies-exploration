import enum
import re
from pprint import pprint
from collections import deque

from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Iterable, Deque


@enum.unique
class TokenKind(enum.Enum):
    SKIP = "SKIP"
    NEW_LINE = "NEW_LINE"
    NUMBER = "NUMBER"
    DEFINE = "DEFINE"
    IDENTIFIER = "IDENTIFIER"
    LITERAL_NUMBER = "LITERAL_NUMBER"
    OP_ASSIGN = "OP_ASSIGN"
    OP_ADDITION = "OP_ADDITION"
    PRINT = "PRINT"


@dataclass(frozen=True)
class Token:
    kind: TokenKind
    value: Optional[str]

    def __str__(self) -> str:
        return f"Token({self.kind.name} | {self.value})"


@dataclass(frozen=True)
class TreeNode:
    token: Optional[Token]
    children: List['TreeNode'] = field(default_factory=list)

    def as_str(self, level: int = 1) -> str:
        return (
            f"Node - {self.token}\n"
            + "".join([
                '\t' * level +
                f"{child.as_str(level=level + 1)}"
                for child in self.children
            ])
        )


@dataclass(frozen=True)
class AbstractSyntaxTree:
    head: TreeNode

    def __str__(self) -> str:
        return (
            f"AST - Program\n"
            f"{self.head.as_str()}"
        )


def lex(source_code: str) -> Tuple[Token, ...]:
    tokens: List[Token] = []

    token_specification = [
        (TokenKind.SKIP, r"[ \t]+"),
        (TokenKind.NEW_LINE, r"\n"),
        (TokenKind.LITERAL_NUMBER, r"\d+"),
        (TokenKind.DEFINE, r"be"),
        (TokenKind.OP_ASSIGN, r"="),
        (TokenKind.OP_ADDITION, r"add"),
        (TokenKind.PRINT, r"print"),
        (TokenKind.IDENTIFIER, r"[a-zA-Z]\w*"),
    ]

    tok_regex = '|'.join(
        f'(?P<{kind.value}>{pattern})'
        for kind, pattern in token_specification
    )

    print("REGEX", tok_regex)
    print("=" * 40)

    for match in re.finditer(tok_regex, source_code):
        kind_str: str = match.lastgroup
        value: str = match.group()

        print("lexed", kind_str, value.strip())

        kind: TokenKind = TokenKind(kind_str)
        token: Token = Token(kind=kind, value=value)
        tokens.append(token)

    print("=" * 40)

    return tuple(tokens)


def simplify_tokens(tokens: Iterable[Token]) -> List[Token]:

    remainder_tokens = deque(tokens)
    simplified = []

    previous_was_new_line = False
    while len(remainder_tokens) > 0:
        token = remainder_tokens.popleft()
        if token.kind == TokenKind.NEW_LINE:
            if previous_was_new_line:
                continue
            previous_was_new_line = True
        elif token.kind == TokenKind.SKIP:
            continue
        else:
            if previous_was_new_line:
                previous_was_new_line = False
                simplified.append(Token(kind=TokenKind.NEW_LINE, value=None))
            simplified.append(token)

    return simplified


def parse_tokens(
    parent_node: TreeNode,
    tokens: Iterable[Token]
) -> Tuple[bool, Deque[TreeNode]]:

    remainder_tokens = deque(tokens)

    is_return = False
    while len(remainder_tokens) > 0:
        token = remainder_tokens.popleft()

        if token.kind == TokenKind.SKIP:
            continue

        elif token.kind == TokenKind.NEW_LINE:
            if parent_node.token is None:
                continue
            return True, remainder_tokens

        elif token.kind == TokenKind.DEFINE:
            define_node = TreeNode(token=token)
            is_return, remainder_tokens = parse_tokens(define_node, remainder_tokens)
            parent_node.children.append(define_node)

        elif token.kind == TokenKind.IDENTIFIER:
            identifier_node = TreeNode(token=token)
            parent_node.children.append(identifier_node)

        elif token.kind == TokenKind.LITERAL_NUMBER:
            literal_number_node = TreeNode(token=token)
            parent_node.children.append(literal_number_node)
            return False, remainder_tokens

        elif token.kind == TokenKind.OP_ASSIGN:
            assignment_node = TreeNode(token=token)
            parent_node.children.append(assignment_node)

        elif token.kind == TokenKind.OP_ADDITION:
            addition_node = TreeNode(token=token)
            is_return, remainder_tokens = parse_tokens(addition_node, remainder_tokens)
            parent_node.children.append(addition_node)

        elif token.kind == TokenKind.PRINT:
            print_node = TreeNode(token=token)
            is_return, remainder_tokens = parse_tokens(print_node, remainder_tokens)
            parent_node.children.append(print_node)

        if is_return and parent_node.token is not None:
            return True, remainder_tokens

    return False, remainder_tokens


def parse(tokens: Iterable[Token]) -> AbstractSyntaxTree:
    program = TreeNode(token=None)
    parse_tokens(program, tokens)
    return AbstractSyntaxTree(head=program)


def do_expression(expression: Iterable[TreeNode]) -> str:
    output_code = ""

    first_child = expression[0]

    if first_child.token.kind == TokenKind.LITERAL_NUMBER:
        output_code += f"{first_child.token.value}"
    elif first_child.token.kind == TokenKind.OP_ADDITION:
        pass
        # first_argument_code = do_expression(first_child.children[0])
        # second_argument_code = do_expression(first_child.children[1])
        # output_code += f"{first_argument_code} + {second_argument_code}"

    output_code += "\n"
    return output_code


def do_define(node: TreeNode) -> str:
    output_code = ""
    identifier = node.children[0].token.value
    output_code += f"{identifier} = "

    expression = node.children[2:]
    output_code += do_expression(expression)

    output_code += "\n"
    return output_code


def do_print(node: TreeNode) -> str:
    output_code = ""
    identifier = node.children[0].token.value
    output_code += f"print({identifier})"
    output_code += "\n"
    return output_code


def generate_code(abstract_syntax_tree: AbstractSyntaxTree) -> str:
    output_code = ""
    for node in abstract_syntax_tree.head.children:

        if node.token.kind == TokenKind.DEFINE:
            output_code += do_define(node)

        elif node.token.kind == TokenKind.PRINT:
            output_code += do_print(node)

    return output_code


def compile(input_file_path: str, output_file_path: str):

    source_code: Optional[str] = None

    with open(input_file_path, "r") as input_file:
        source_code = input_file.read()

    if source_code is None:
        print("No source code!")
        return

    print("Source code")
    print("=" * 40)
    print(source_code)
    print("=" * 40)

    print("Lexing ...")
    tokens = lex(source_code)
    print("Tokens")
    print("=" * 40)
    pprint(tokens)
    print("=" * 40)

    print("Simplify ...")
    tokens = simplify_tokens(tokens)
    print("Simplified tokens")
    print("=" * 40)
    pprint(tokens)
    print("=" * 40)

    print("Parsing ...")
    tree = parse(tokens)
    print("=" * 40)
    print(tree)

    print("Generate code ...")
    output_code = generate_code(tree)
    print("=" * 40)
    print(output_code)
    print("=" * 40)
