# START WITH TM PACKET IN BYTES
python3 ./tools/analyze_cadu.py ./data/SPPencaps_CFDP_metadata_tx.bin 

# CHANGE IT TO HEX FOR VIEWING (WITH EXAMPLE)
python3 ./tools/dump_frame.py ./data/SPPencaps_CFDP_metadata_tx.bin  1115 > ./data/SPPencaps_CFDP_metadata_tx.hex

00000000  18 b3 c0 00 00 89 02 00 00 01 00 01 30 2e 32 31
00000010  2f 64 61 74 61 2f 00 00 00 00 00 00 00 00 00 00
00000020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00000030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00000040  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00000050  2f 74 6d 70 2f 64 61 74 61 00 00 00 00 00 00 00
00000060  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00000070  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00000080  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00


## TROUBLESHOOTING sync_coding_v0
# SHIP IT (SEND PACKET THROUGH EACH CHAIN)
python3 ./grc/sync_coding/sync_coding_v0.py
python3 ./grc/cat_A_tx/cat_A_tx_v0.py
python3 ./grc/Rx_TM/new_rx_chain_v0.py

# COMPARE FRAMES + LOOK FOR ASM
python3 ./tools/analyze_cadu.py ./data/art/tm_out.bin   1115

python3 ./tools/analyze_cadu.py ./data/art/rand_out.bin 1115

python3 ./tools/analyze_cadu.py ./data/art/rs_out.bin   1275

python3 ./tools/analyze_cadu.py ./data/art/asm_out.bin  1279

python3 ./tools/analyze_cadu.py ./data/art/conv_out.bin 2558

# VIEW HEX FRAME
python3 ./tools/dump_frame.py ./data/art/tag_out.bin  1115 > ./data/art/tag_frame0.hex

python3 ./tools/dump_frame.py ./data/art/tm_out.bin  1115 > ./data/art/tm_frame0.hex

python3 ./tools/dump_frame.py ./data/art/rs_out.bin  1275 > ./data/art/rs_frame0.hex

python3 ./tools/dump_frame.py ./data/art/asm_out.bin 1279 > ./data/art/asm_frame0.hex

## TROUBLESHOOTING cat_A_tx_V0

## TROUBLESHOOTING new_rx_chain_v0



