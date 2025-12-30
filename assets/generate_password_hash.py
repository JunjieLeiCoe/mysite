#!/usr/bin/env python3
"""
Generate SHA-256 hash for password-protected Hugo posts
Usage: python3 generate_password_hash.py
"""

import hashlib
import getpass

def generate_hash(password):
    """Generate SHA-256 hash of password"""
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
    print("=" * 50)
    print("Hugo Password Hash Generator")
    print("=" * 50)
    
    password = getpass.getpass("Enter password: ")
    confirm = getpass.getpass("Confirm password: ")
    
    if password != confirm:
        print("❌ Passwords don't match!")
        exit(1)
    
    hash_value = generate_hash(password)
    
    print("\n✅ Password hash generated!\n")
    print("Add this to your post's front matter:\n")
    print("---")
    print("title: \"Your Title\"")
    print("date: 2024-01-01")
    print('layout: "protected"')
    print(f'password_hash: "{hash_value}"')
    print("---")
    print("\n" + "=" * 50)

