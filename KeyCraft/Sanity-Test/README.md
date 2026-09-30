# Sanity Test

**Category:** KeyCraft / Physical Security  
**Difficulty:** Easy  
**Status:** Solved

## Challenge

A photograph of a physical key was provided. The goal was to identify the key type and determine its cut pattern using the challenge's required flag format.

## Tools Used

- Visual inspection
- Basic knowledge of key bitting systems

## Approach

### 1. Identify the key type

The key was stamped **SC1**, identifying it as a Schlage C keyway. SC1 keys use five cut positions.

### 2. Read the cut depths

I examined the blade from the shoulder toward the tip and estimated the relative depth of each cut.

| Position | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Estimated depth | 4 | 5 | 4 | 4 | 6 |

### 3. Format the answer

Using the identified key type and cut sequence, I formatted the result according to the challenge's required structure and successfully completed the challenge.

## What I Learned

- How physical key markings can identify the keyway
- How key bitting and cut-depth systems are represented
- How to estimate cut depths visually from a photograph
- How physical-security concepts can appear in CTF competitions alongside software-focused challenges
