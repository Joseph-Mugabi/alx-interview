# UTF-8 Validation
### UTF-8 is a variable-width character encoding that can represent 
### any character in the Unicode standard. It is widely used and has become
### the dominant character encoding for the web and many modern software 
### systems.

```
To determine if a given data set represents a valid UTF-8 encoding, we can follow these steps:

1. Initialize a variable bytes_to_follow to 0. This variable will keep 
track of the number of bytes to follow for a multi-byte character.

2. Iterate through each integer in the data set:

Check if bytes_to_follow is greater than 0. If so, it means we are currently parsing
a multi-byte character. In this case, check if the two most significant bits of the
current integer are "10" (indicating a continuation byte). If not, return False,
as it is not a valid UTF-8 encoding.
If bytes_to_follow is 0, it means we are starting a new character. Determine the number
of bytes to follow based on the two most significant bits of the current integer.
If the two most significant bits are "0", it means it is a single-byte character (1 byte in total).
If the two most significant bits are "110", it means it is a two-byte character (1 byte to follow).
If the two most significant bits are "1110", it means it is a three-byte character (2 bytes to follow).
If the two most significant bits are "11110", it means it is a four-byte character (3 bytes to follow).
Update bytes_to_follow accordingly.

3. After each iteration, decrement bytes_to_follow by 1, indicating that we have processed one byte of
the multi-byte character.

4. If at any point bytes_to_follow becomes negative or greater than 0, return False,
as it indicates an incomplete or invalid multi-byte character.

5. If we reach the end of the data set and bytes_to_follow is 0, return True,
as it indicates that all characters were successfully parsed and it is a valid UTF-8 encoding.
```

or
```
1. state_of_bytes is a variable used to keep track of the number of bytes needed to represent 
the current character being processed. It is initialized to 0.

2. The function iterates over each num (integer) in the data list, representing each 
byte in the UTF-8 encoded data.

3. The variable bit is set to the binary value 0b10000000, which is the most significant 
bit of an 8-bit byte. This bit is used to determine the number of bytes needed to represent a character.

4. If state_of_bytes is 0 (meaning a new character is starting):

a. The function checks the most significant bits of the byte (num) by repeatedly 
shifting the bit to the right and checking if it's set (bitwise AND operation).
 This determines the number of bytes needed to represent the character, and state_of_bytes is updated accordingly.

b. If state_of_bytes exceeds 4, it means the character is represented by more than 4 bytes, 
which is not a valid UTF-8 encoding, so the function returns False.

c. If state_of_bytes is nonzero (meaning it's greater than 0),
it decrements the state_of_bytes counter by 1, as one byte has already been processed.

d. If state_of_bytes becomes 0 (indicating a valid character),
it returns False because a new character should have started.

5. If state_of_bytes is greater than 0 (meaning we are in the middle of processing a character):

a. The function checks that the current byte (num) starts with the binary pattern 10xxxxxx,
which indicates a continuation byte in UTF-8. If not, it means the byte is either a new character
start or an invalid byte sequence, and the function returns False.

b. The state_of_bytes counter is decremented by 1, indicating that one byte of the character has been processed.

After processing all the bytes, if there are no remaining bytes to complete the last character (i.e., state_of_bytes is 0), 
it means the encoding is valid, and the function returns True. Otherwise, it returns False.
```