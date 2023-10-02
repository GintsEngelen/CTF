
# Assuming your little-endian hex string is in LE_hex
LE_hex="09ea14900804b000080489c3f7f6cd80ffffffff0000000109e9f160f7f7a110f7f6cdc70000000009ea01800000000109ea147009ea14906f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3266633130613130ff98007df7fa7af8f7f7a440fc761c000000000100000000f7e09ce9f7f7b0c0f7f6c5c0f7f6c000ff981048f7dfa68df7f6c5c008048ecaff98105400000000f7f8ef090804b000f7f6c000f7f6ce20ff981088f7f94d50f7f6d890fc761c00f7f6c0000804b000ff98108808048c8609e9f160ff981074ff98108808048be9f7f6c3fc00000000ff98113cff981134000000010000000109e9f160fc761c00ff9810a00000000000000000f7daffa1f7f6c000f7f6c00000000000"

GE_hex = ""

for i in range(0, len(LE_hex), 8):
    hex_chars_buffer = LE_hex[i:i+8]
    GE_hex += hex_chars_buffer[6:8]
    GE_hex += hex_chars_buffer[4:6]
    GE_hex += hex_chars_buffer[2:4]
    GE_hex += hex_chars_buffer[0:2]

print(GE_hex)

