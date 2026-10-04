import subprocess

#.encode() converts string into raw bytes .decode() converts raw bytes into string. These two still confuse me because the output is not even in binary

password = input("Enter the password that you want to convert into a NT-Hash\n")

utf16le = password.encode("utf-16le")

result = subprocess.run(
    ["openssl", "dgst", "-provider", "legacy", "-md4"],
    input=utf16le,
    capture_output=True, #captures the stdout and stderr, you can set it to false and compare print(result) with True vs False
)


#print(result)
#print(result.stdout)
#print(result.stdout.decode())
#print(result.stdout.decode().strip())
#print(result.stdout.decode().strip().split("="))
#print(result.stdout.decode().strip().split("=")[1])
print(f"\nThe NT-HASH for {password} is:\n{result.stdout.decode().strip().split("=")[1].strip()}")