def spreadsheet_decoding(spreedsheet):
    """
    Given a spreadsheet column string like AA, AZ etc,
    decode it into its numeric value
    """
    value = 0
    for c in spreedsheet:
        value = value * 26 + ord(c) - ord("A") + 1
    return value


print(spreadsheet_decoding("AA"))
