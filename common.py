def load(filename):
    return [i.strip() for i in open(f"sources/{filename}.txt").readlines() if i.strip() and not i.startswith("//")]

def testload(filename):
    return ["%s %s" % (i.strip(), "xyz") for i in open(f"sources/{filename}.txt").readlines() if i.strip() and not i.startswith("//")]

