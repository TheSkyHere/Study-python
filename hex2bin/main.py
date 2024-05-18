def hex_to_bin(hex_file, bin_file):
    with open(hex_file, 'r') as f:
        hex_data = f.read().strip().split(':')

    with open(bin_file, 'wb') as f:
        for line in hex_data:
            print(line)
            # if line.startswith(':'):
            bytes_data = bytes.fromhex(line[1:])
            print(line)
            f.write(bytes_data)

def main():
    # hex_file = input("请输入Hex文件路径：")
    # bin_file = input("请输入要保存的Bin文件路径：")
    hex_to_bin("/home_b/matao/H6321-1512.hex", "/home_b/matao/H6321-1512.bin")
    print("Hex文件已成功转换为Bin文件！")

if __name__ == "__main__":
    main()