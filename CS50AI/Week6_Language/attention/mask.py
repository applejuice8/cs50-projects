def get_mask_token_index(mask_token_id, inputs):
    """
    Return the index of the token with the specified `mask_token_id`, or
    `None` if not present in the `inputs`.
    """
    # TODO: Implement this function
    input_ids = inputs['input_ids'][0]

    for i, input_id in enumerate(input_ids):
        if input_id == mask_token_id:
            return i
    return None


def get_color_for_attention_score(attention_score):
    """
    Return a tuple of three integers representing a shade of gray for the
    given `attention_score`. Each value should be in the range [0, 255].
    """
    # TODO: Implement this function
    color = int(attention_score * 255.0)
    return (color, color, color)


def visualize_attentions(tokens, attentions):
    """
    Produce a graphical representation of self-attention scores.

    For each attention layer, one diagram should be generated for each
    attention head in the layer. Each diagram should include the list of
    `tokens` in the sentence. The filename for each diagram should
    include both the layer number (starting count from 1) and head number
    (starting count from 1).
    """
    # TODO: Update this function to produce diagrams for all layers and heads.
    for layer in range(len(attentions)):
        for head in range(attentions[0].shape[1]):
            generate_diagram(
                layer + 1,
                head + 1,
                tokens,
                attentions[layer][0][head]
            )
