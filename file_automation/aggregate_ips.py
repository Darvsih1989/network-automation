import glob

# Path to all txt files containing IPs
files = glob.glob("acl/generated_files/*.txt")

aggregated_ips = set()
for file in files:
    with open(file) as f:
        for line in f:
            ip = line.strip()
            if ip:
                aggregated_ips.add(ip)

# Save aggregated IPs
with open("aggregated_ips_all.txt", "w") as f:
    for ip in sorted(aggregated_ips):
        f.write(ip + "\n")

print("Aggregated IPs saved in aggregated_ips_all.txt")