import argparse
from concurrent.futures import ThreadPoolExecutor

SUPPORTED = {".pdf", ".docx", ".txt"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bucket", required=True)
    ap.add_argument("--workers", type=int, default=8, help="parallel workers")
    ap.add_argument("--dry-run", action="store_true", help="list without indexing")
    args = ap.parse_args()

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        # ... index each supported file in parallel ...
        pass


if __name__ == "__main__":
    main()
