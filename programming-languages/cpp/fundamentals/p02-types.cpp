#include <iostream>
#include <limits>
#include <cfloat>
#include <fmt/format.h>

using namespace std;

const string ANY_FORMAT = "{:.<30} {:}\n";
const string DECIMAL_FORMAT = "{:.<30} {:d}\n";
const string FLOAT_FORMAT = "{:.<30} {:f}\n";

int main(int argc, char const *argv[]) {
    char char_val = CHAR_MAX;
    fmt::print(DECIMAL_FORMAT, "CHAR ", char_val);

    signed char schar_val = SCHAR_MIN;
    fmt::print(DECIMAL_FORMAT, "SIGNED CHAR ", schar_val);

    unsigned char uchar_max_val = UCHAR_MAX;
    fmt::print(DECIMAL_FORMAT, "UNSIGNED CHAR MAX ", uchar_max_val);

    short short_val = SHRT_MAX;
    fmt::print(DECIMAL_FORMAT, "SHORT MAX ", short_val);

    signed short sshort_min_val = SHRT_MIN;
    signed short sshort_max_val = SHRT_MAX;
    fmt::print(DECIMAL_FORMAT, "SIGNED SHORT MIN ", sshort_min_val);
    fmt::print(DECIMAL_FORMAT, "SIGNED SHORT MAX ", sshort_max_val);

    unsigned short ushort_max_val = USHRT_MAX;
    fmt::print(DECIMAL_FORMAT, "UNSIGNED SHORT MAX ", ushort_max_val);

    int int_val = INT_MAX;
    fmt::print(DECIMAL_FORMAT, "INT MAX ", int_val);

    signed int sint_min_val = INT_MIN;
    signed int sint_max_val = INT_MAX;
    fmt::print(DECIMAL_FORMAT, "SIGNED INT MIN ", sint_min_val);
    fmt::print(DECIMAL_FORMAT, "SIGNED INT MAX ", sint_max_val);

    unsigned int uint_max_val = UINT_MAX;
    fmt::print(DECIMAL_FORMAT, "UNSIGNED INT MAX ", uint_max_val);

    long long_min_val = LONG_MIN;
    long long_max_val = LONG_MAX;
    fmt::print(DECIMAL_FORMAT, "LONG MIN ", long_min_val);
    fmt::print(DECIMAL_FORMAT, "LONG MAX ", long_max_val);

    signed long slong_min_val = LONG_MIN;
    signed long slong_max_val = LONG_MAX;
    fmt::print(DECIMAL_FORMAT, "SIGNED LONG MIN ", slong_min_val);
    fmt::print(DECIMAL_FORMAT, "SIGNED LONG MAX ", slong_max_val);

    unsigned long ulong_max_val = ULONG_MAX;
    fmt::print(DECIMAL_FORMAT, "UNSIGNED LONG MAX ", ulong_max_val);

    long long llong_min_val = LLONG_MIN;
    long long llong_max_val = LLONG_MAX;
    fmt::print(DECIMAL_FORMAT, "LONG LONG MIN ", llong_min_val);
    fmt::print(DECIMAL_FORMAT, "LONG LONG MAX ", llong_max_val);

    signed long long sllong_max_val = LLONG_MAX;
    fmt::print(DECIMAL_FORMAT, "SIGNED LONG LONG MAX ", sllong_max_val);

    unsigned long long ullong_max_val = ULLONG_MAX;
    fmt::print(DECIMAL_FORMAT, "UNSIGNED LONG LONG MAX ", ullong_max_val);

    float float_val = FLT_MAX;
    fmt::print(FLOAT_FORMAT, "FLOAT MAX ", float_val);

    cout << endl;

    double double_val = DBL_MAX;
    fmt::print(FLOAT_FORMAT, "DOUBLE MAX ", double_val);

    cout << endl;

    long double ldouble_val = LDBL_MAX;
    fmt::print(FLOAT_FORMAT, "LONG DOUBLE MAX ", ldouble_val);

    return 0;
}
