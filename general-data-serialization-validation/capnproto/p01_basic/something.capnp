@0xe74da7ecaf9ba1b3;  # generated with capnp id

struct Thing {
    title @0 :Text;
    val @1 :UInt16;

    stuff @2 :List(InnerThing);

    struct InnerThing {
        kek @0 :UInt16;
        lol @1 :PotatoType;

        enum PotatoType {
            red @0;
            white @1;
            transparent @2;
        }
    }
}
