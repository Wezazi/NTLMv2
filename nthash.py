import subprocess

password = input("Enter the password that you want to convert into a NT-Hash\n")

utf16le = password.encode("utf-16le")

result = subprocess.run(
    ["openssl", "dgst", "-provider", "legacy", "-md4"],
    input=utf16le,
    capture_output=True,
)

ntHash = result.stdout.decode().strip().split("=")[1].strip()

print(f"\nThe NT-HASH for {password} is:\n{ntHash}")