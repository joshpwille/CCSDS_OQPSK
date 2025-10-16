# add near the other imports
from gnuradio import gr, pdu
import pmt

class pdu_drop_head_asm(gr.basic_block):
    def __init__(self, n_drop=4):
        gr.basic_block.__init__(self,
            name="pdu_drop_head_asm",
            in_sig=None, out_sig=None)
        self.message_port_register_in(pmt.intern('in'))
        self.message_port_register_out(pmt.intern('out'))
        self.set_msg_handler(pmt.intern('in'), self.handle)

        self.n_drop = n_drop

    def handle(self, msg):
        meta = pmt.to_python(pmt.car(msg)) or {}
        vec  = pmt.cdr(msg)
        b    = bytearray(pmt.u8vector_elements(vec))
        if len(b) >= self.n_drop:
            b = b[self.n_drop:]           # strip 4-byte ASM
        outp = pmt.cons(pmt.to_pmt(meta), pmt.init_u8vector(len(b), b))
        self.message_port_pub(pmt.intern('out'), outp)

