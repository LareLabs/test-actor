#!/usr/bin/env python3
"""
Simple test actor to verify Apify Docker builds work.
"""
import sys

def main():
    print("Test actor started successfully!")
    print("Python version:", sys.version)
    print("Test completed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())