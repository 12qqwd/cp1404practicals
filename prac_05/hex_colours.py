HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}


def main():
    colour_name = input("Enter a colour name (or blank to quit): ").strip().lower()

    while colour_name != "":
        hex_code = HEX_COLOURS.get(colour_name)
        if hex_code:
            print(f"{colour_name} is {hex_code}")
        else:
            print(f"Sorry, '{colour_name}' is not a known colour.")
        colour_name = input("Enter a colour name (or blank to quit): ").strip().lower()


if __name__ == "__main__":
    main()
