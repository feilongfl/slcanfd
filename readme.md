
# slcanfd

A serial line CAN-FD interface driver for linux.

## protocol

A CAN frame has a can_id (11 bit standard frame format OR 29 bit extended
frame format) a data length code (len) which can be from 0 to 8
and up to `len` data bytes as payload.
Additionally a CAN frame may become a remote transmission frame if the
RTR-bit is set. This causes another ECU to send a CAN frame with the
given can_id.

The SLCAN ASCII representation of these different frame types is:
`type` `id` `dlc` `data`*

Extended frames (29 bit) are defined by capital characters in the type.
RTR frames are defined as 'r' types - normal frames have 't' type.
CAN-FD with BRS are defined as 'x',without BRS are defined as 'X':

- t => 11 bit data CAN frame
- r => 11 bit RTR CAN frame
- T => 29 bit data CAN frame
- R => 29 bit RTR CAN frame
- tx => 11 bit data CAN-FD frame(with BRS)
- rx => 11 bit RTR CAN-FD frame(with BRS)
- Tx => 29 bit data CAN-FD frame(with BRS)
- Rx => 29 bit RTR CAN-FD frame(with BRS)
- tX => 11 bit data CAN-FD frame(without BRS)
- rX => 11 bit RTR CAN-FD frame(without BRS)
- TX => 29 bit data CAN-FD frame(without BRS)
- RX => 29 bit RTR CAN-FD frame(without BRS)

The `id` is 3 (standard) or 8 (extended) bytes in ASCII Hex (base64).
The `dlc` is a one byte Hex number ('0' - 'f')
The `data` section has at much ASCII Hex bytes as defined by the `dlc`

### Examples:

- t1230 : can_id 0x123, len 0, no data
- t4563112233 : can_id 0x456, len 3, data 0x11 0x22 0x33
- T12ABCDEF2AA55 : extended can_id 0x12ABCDEF, len 2, data 0xAA 0x55
- r1230 : can_id 0x123, len 0, no data, remote transmission request
- tx1230 : can_id 0x123, len 0, no data, can-fd, use BRS
- TX12ABCDEF2AA55 : extended can_id 0x12ABCDEF, len 2, data 0xAA 0x55, can-fd, not use BRS
- rX1230 : can_id 0x123, len 0, no data, remote transmission request, can-fd
