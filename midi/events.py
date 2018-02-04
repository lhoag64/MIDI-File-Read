# <MThd Chunk> = <MThd><Fmt><Track Cnt><Divsion> (16-bit values)
# <MTrk Chunk> = <MTrk><len><MTrk Event>+
# <MTrak Event> = <delta-time(VLQ)><Event>
# <delta-time> = variable-lenght-quantity (VLQ)
# <Event> = <MIDI Event>|<Sysex Event>|<Meta Event>
# <MIDI Event>
# <Sysex Event> = <FO><len(VLQ)><bytes>|<F7><len(VLQ)><bytes>
# <Meta Event> = <FF><type><len><bytes>

# Meta Events
# FF 00 02 SeqNum
# FF 01 len text Event
# FF 02 len text Copyright Notice
# FF 03 len text Sequence/Track Name
# FF 04 len text Instrument Name
# FF 05 len text Lyric
# FF 06 len text Marker
# FF 07 len text Cue Point
# FF 20 01 cc MIDI Channel Prefix
# FF 2F 00 End of Track
# FF 51 02 tttttt Set Tempo
# FF 54 05 hr mn se fr ff SMPTE Offset
# FF 58 04 nn dd cc bb Time Signature
# FF 59 02 sf mi Key Signature
# FF 7F len data Sequencer Specific Meta-Event
# MIDI Events
#
