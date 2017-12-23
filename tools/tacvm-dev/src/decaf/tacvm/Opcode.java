package decaf.tacvm;

public enum Opcode {
	ASSIGN, ADD, SUB, MUL, DIV, MOD, EQU, NEQ, LES, LEQ, GTR, GEQ, NEG, LAND,
	LOR, LNOT, BRANCH, BEQZ, BNEZ, LIB_CALL, DIRECT_CALL, INDIRECT_CALL, RETURN, LOAD,
	STORE, LOAD_VTBL, LOAD_IMM4, LOAD_STR, ENTER_FUNC, LEAVE_FUNC,
	MOVE_FROM_RV, PARM
}
