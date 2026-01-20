import json, hashlib, os, sys
REPORT, ARTIFACT, README = "certification_report.json", "certification_final.json", "README.md"
def short_hash(path):
    with open(path, "rb") as f: return hashlib.sha256(f.read()).hexdigest()[:8]
def main():
    if not all(os.path.exists(p) for p in (REPORT, ARTIFACT, README)):
        print("❌ Missing Files"); sys.exit(2)
    h = short_hash(REPORT)
    art_h = json.load(open(ARTIFACT)).get("audit_hash")
    rdme = open(README).read()
    ok = (art_h == h and h in rdme)
    print(f"--- 🛰️ DECATUR VERIFICATION: {h} ---")
    if ok: print("\n🏆 CHAIN VERIFIED. Node is Solid Concrete."); sys.exit(0)
    else: print("\n⚠️ CHAIN BROKEN."); sys.exit(1)
if __name__ == "__main__": main()
