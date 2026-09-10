from formatter import format_json

print("🧹 JSON Pretty Printer")
print("=" * 35)

data = input("Paste JSON: ")

try:
    print("\n✨ Formatted JSON:\n")
    print(format_json(data))
except ValueError:
    print("\n❌ Invalid JSON.")
