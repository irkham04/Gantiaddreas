import re

# Baca konfigurasi lama
with open("active_all.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

# Baca file alamat baru
with open("new_addresses.txt", "r", encoding="utf-8") as f:
    new_addresses = f.read().splitlines()

# Fungsi ganti alamat
def replace_address(line, new_address):
    line = re.sub(r'(@)[^:@]+', r'\1' + new_address, line)
    line = re.sub(r'(host=)[^&]+', r'\1' + new_address, line)
    line = re.sub(r'(add=)[^&]+', r'\1' + new_address, line)
    line = re.sub(r'(sni=)[^&]+', r'\1' + new_address, line)
    return line

# Ganti semua baris
new_lines = []
for i, line in enumerate(lines):
    addr = new_addresses[i % len(new_addresses)]
    new_lines.append(replace_address(line, addr))

# Simpan hasil
with open("active_all_updated.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines))

print("Selesai! File updated sudah dibuat: active_all_updated.txt")
