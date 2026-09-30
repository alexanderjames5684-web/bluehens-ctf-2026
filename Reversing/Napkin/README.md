# Napkin

**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Status:** Attempted

## Challenge

The challenge provided a low-resolution image of a hand-drawn logic circuit with the prompt:

> I found this circuit drawn on a napkin, can you help me find out how to turn it on?

The goal was to determine the binary input combination that would activate the circuit output.

## Tools / Techniques Explored

- Image enhancement
- Logic-circuit analysis
- Python imaging tools
- OCR experimentation

## What I Observed

The circuit appeared to contain:

- Roughly 10 binary input lines
- Multiple AND gates checking combinations of inputs
- Inverted inputs in several locations
- A final output stage combining the gate results

This suggested a combinational logic problem where tracing the circuit or recreating it in a simulator could reveal the valid input pattern.

## Attempted Approach

### 1. Improve the source image

Because the provided circuit image was difficult to read, I experimented with:

- Upscaling the image
- Contrast enhancement
- Sharpening
- Black-and-white thresholding
- OCR on the input-label area

The low source resolution made the labels and some wire connections too ambiguous to reconstruct reliably.

### 2. Analyze the visible gate structure

I identified the general AND/NOT structure and tried to trace which input combinations fed each branch of the circuit.

The main blocker was not understanding the logic-gate concepts, but being unable to confidently distinguish several wires and labels in the provided image.

### 3. Consider circuit simulation

A logic simulator such as Logisim would be a practical way to verify the circuit once the connections are reconstructed accurately.

## Outcome

I did **not** fully solve this challenge during the event. I am keeping the writeup because it documents the reverse-engineering approach I attempted and the technical obstacle that prevented a reliable final answer.

## What I Learned

- How to break a combinational logic circuit into smaller gates and branches
- How AND, NOT, NAND, and NOR-style logic affect binary outputs
- How image quality can become part of the reverse-engineering problem
- When recreating a system in a simulator can be more efficient than solving it entirely by inspection
