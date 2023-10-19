from src import betafold_3_amino_analyzer


def run_amino_analyzer(sequence: str, procedure: str, *, weight_type: str = 'average', enzyme: str = 'trypsin'):
    '''
    This is the main function to run the amino-analyzer.py tool
    
    Parameters:
    - sequence (str): amino acid sequence in one-letter code
    - procedure (str): amino-analyzer.py tool has 5 functions at all:
        1. aa_weight - Calculates the amino acids weight in a protein sequence. Return float weight
            weight_type = 'average': default argument for 'aa_weight' function
            weight_type = 'monoisotopic' can be used as a second option
        2. count_hydroaffinity - Counts the quantity of hydrophobic and hydrophilic amino acids in a protein sequence. Return list in order: hydrophobic, hydrophilic
        3. peptide_cutter - Identifies cleavage sites in a given peptide sequence using a specified enzyme. Return list of cleavage sites
            enzyme = 'trypsin': default argument for 'peptide_cutter' function
            enzyme = 'chymotrypsin' can be used as a second option
        4. one_to_three_letter_code - Converts a protein sequence from one-letter amino acid code to three-letter code. Return string of amino acids in three-letter code
        5. sulphur_containing_aa_counter - Counts sulphur-containing amino acids in a protein sequence. Return quantaty of sulphur-containing amino acids

    Returns:
    - The result of the specified procedure
    '''

    procedures = ['aa_weight', 'count_hydroaffinity', 'peptide_cutter', 'one_to_three_letter_code', 'sulphur_containing_aa_counter']
    if procedure not in procedures:
        raise ValueError(f'Incorrect procedure. Acceptable procedures: {", ".join(procedures)}')

    if not is_aa(sequence):
        raise ValueError('Incorrect sequence. Only amino acids are allowed (V, I, L, E, Q, D, N, H, W, F, Y, R, K, S, T, M, A, G, P, C, v, i, l, e, q, d, n, h, w, f, y, r, k, s, t, m, a, g, p, c).')

    if procedure == 'aa_weight':
        result = aa_weight(sequence, weight_type)
    elif procedure == 'count_hydroaffinity':
        result = count_hydroaffinity(sequence)
    elif procedure == 'peptide_cutter':
        result = peptide_cutter(sequence, enzyme)
    elif procedure == 'one_to_three_letter_code':
        result = one_to_three_letter_code(sequence)
    elif procedure == 'sulphur_containing_aa_counter':
        result = sulphur_containing_aa_counter(sequence)
    return result