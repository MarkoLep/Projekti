def kuusi(koko):
    print("tämä on kuusi")
    for i in range(koko):
        oksat = 2 * i + 1
        välilyönnit = koko - i - 1
        print(" " * välilyönnit + "*" * oksat)
    print(" " * (koko - 1) + "*")
kuusi(10)