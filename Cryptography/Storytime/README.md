# Storytime

**Category:** Cryptography  
**Difficulty:** Medium  
**Status:** Solved

## Challenge

Two files were provided:

- `storytime.txt` — a short story containing clues about the encoding chain
- `ciphertext.txt` — an encoded ciphertext

The challenge required identifying the transformations hinted at by the story and reversing them in the correct order.

## Tools Used

- Python 3
- CyberChef

## Key Clues

The wording in the story hinted at several common encoding and transformation techniques:

| Story clue | Interpretation |
|---|---|
| "4 chunks away" | Base64 clue |
| "exorcise" | XOR clue |
| "little less than two weeks" / "rotting" | ROT13 clue |
| "bashing my head into a wall" | Base/hex encoding clue |
| "stabbed me in the back" | Reversal/layering clue |

## Approach

### 1. Decode the outer hexadecimal layer

The ciphertext began as hexadecimal text. I first converted it from hex into readable text.

```python
step1 = bytes.fromhex(ciphertext).decode()
```

This revealed another encoded layer.

### 2. Decode the Base64 layer

The next layer was recognizable as Base64.

```python
import base64
step2 = base64.b64decode(step1).decode()
```

### 3. Continue peeling back layers

The result exposed additional encoded data. I continued reversing the chain using the clues from the story, including hex decoding and the transformations hinted at by XOR/ROT13 references.

The important part of the challenge was recognizing that the flavor text was effectively an instruction sheet for the decoding order.

## What I Learned

- How to identify nested encoding layers
- How challenge flavor text can hide technical instructions
- How to combine Python and CyberChef for iterative decoding
- How to reason through multi-step cryptography challenges instead of treating each layer independently

> I intentionally left the flag out of this writeup because the copy I preserved had an inconsistent flag value. The solve itself is documented here without publishing uncertain information.
