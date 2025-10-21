#!/usr/bin/env python3
"""
Insert or append a single-page slide PDF into a dissertation PDF.

Usage:
  python tools/insert_slide.py dissertation.pdf slide.pdf out.pdf        # append slide to end
  python tools/insert_slide.py dissertation.pdf slide.pdf out.pdf 3    # insert AFTER page 3 (1-based)
"""
import sys
from pikepdf import Pdf

def main():
    if len(sys.argv) < 4:
        print("Usage: insert_slide.py dissertation.pdf slide.pdf out.pdf [insert_after_page]")
        sys.exit(1)

    dissertation_path = sys.argv[1]
    slide_path = sys.argv[2]
    out_path = sys.argv[3]
    insert_after = int(sys.argv[4]) if len(sys.argv) > 4 else None

    with Pdf.open(dissertation_path) as d, Pdf.open(slide_path) as s:
        if insert_after is None:
            # append
            d.pages.extend(s.pages)
        else:
            # insert after page 'insert_after' (1-based)
            if insert_after < 0:
                raise ValueError("insert_after must be >= 0")
            # convert to 0-based index: position to insert is insert_after
            idx = insert_after
            new_pages = d.pages[:idx] + s.pages + d.pages[idx:]
            d.pages.clear()
            d.pages.extend(new_pages)
        d.save(out_path)
        print("Saved merged PDF to:", out_path)

if __name__ == "__main__":
    main()
