#!/usr/bin/env python3
"""Lint commit messages against conventions"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Lint commit messages against conventions")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("commit-linter v0.1.0");return
 print(f"[12:01] commit-linter ready")
if __name__=="__main__":main()
