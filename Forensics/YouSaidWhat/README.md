# You Said What?

**Category:** Forensics  
**Difficulty:** Easy  
**Status:** Solved

## Challenge

A `.pcapng` packet capture was provided with the prompt:

> I think someone called you chicken. You should do something about it.

## Tools Used

- Wireshark
- Python 3

## Approach

### 1. Inspect HTTP objects

I opened the packet capture in Wireshark and used **File → Export Objects → HTTP** to inspect files transferred in the capture.

Among the transferred objects were several decoys along with files such as `whoareyoucalling.zip` and `chicken.jpg`.

### 2. Inspect the image data

The `chicken.jpg` data contained a hex-encoded string:

```text
6e6f626f64792063616c6c73206d6520636869636b656e21
```

Decoding it from hex produced:

```text
nobody calls me chicken!
```

A small Python script is included in the [`files`](./files/) directory to demonstrate the decoding step.

### 3. Use the decoded value

The decoded phrase was used as the password for the password-protected ZIP recovered from the traffic. Extracting the archive revealed the challenge flag.

## What I Learned

- How to export HTTP objects from a packet capture in Wireshark
- How to inspect transferred files for hidden metadata/data
- How to recognize and decode hexadecimal strings
- How artifacts within one network capture can provide clues for other artifacts
