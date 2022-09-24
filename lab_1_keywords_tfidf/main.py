"""
Lab 1
Extract keywords based on frequency related metrics
"""
from typing import Optional, Union
from string import punctuation
from operator import itemgetter
from math import log


def clean_and_tokenize(text: str) -> Optional[list[str]]:
    """
    Removes punctuation, casts to lowercase, splits into tokens

    Parameters:
    text (str): Original text

    Returns:
    list[str]: A sequence of lowercase tokens with no punctuation

    In case of corrupt input arguments, None is returned
    """

    if not isinstance(text, str):
        return None
    for i in punctuation:
        text = text.replace(i, "")
        text = text.lower().strip()
    tokens = text.split()
    print(tokens)
    return tokens


def remove_stop_words(tokens: list[str], stop_words: list[str]) -> Optional[list[str]]:
    """
    Excludes stop words from the token sequence

    Parameters:
    tokens (List[str]): Original token sequence
    stop_words (List[str]: Tokens to exclude

    Returns:
    List[str]: Token sequence that does not include stop words

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(tokens, (str, list)) or not isinstance(stop_words, (list, str)):
        return None
    clean_tokens = []
    for i in tokens:
        if i not in stop_words:
            clean_tokens.append(i)
    print(clean_tokens)
    return clean_tokens


def calculate_frequencies(tokens: list[str]) -> Optional[dict[str, int]]:
    """
    Composes a frequency dictionary from the token sequence

    Parameters:
    tokens (List[str]): Token sequence to count frequencies for

    Returns:
    Dict: {token: number of occurrences in the token sequence} dictionary

    In case of corrupt input arguments, None is returned
    """
    if isinstance(tokens, list) and len(tokens) != 0:
        dictionary = {}
        for word in tokens:
            if type(word) == str:
                if word in dictionary.keys():
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
            else:
                return None
        print(dictionary)
        return dictionary
    else:
        return None


def get_top_n(frequencies: dict[str, Union[int, float]], top: int) -> Optional[list[str]]:
    """
    Extracts a certain number of most frequent tokens

    Parameters:
    frequencies (Dict): A dictionary with tokens and
    its corresponding frequency values
    top (int): Number of token to extract

    Returns:
    List[str]: Sequence of specified length
    consisting of tokens with the largest frequency

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(frequencies, dict) or not isinstance(top, int) or isinstance(top, bool) or not frequencies or top \
            <= 0:
        return None
    for i in frequencies.keys():
        if not isinstance(i, str):
            return None
    for i in frequencies.values():
        if not isinstance(i, int) and not isinstance(i, float):
            return None
        filtered_words = [word for word, freq in sorted(frequencies.items(), key=itemgetter(1), reverse=True)]
        top_n = filtered_words[:top]
        return top_n


def calculate_tf(frequencies: dict[str, int]) -> Optional[dict[str, float]]:
    """
    Calculates Term Frequency score for each word in a token sequence
    based on the raw frequency

    Parameters:
    frequencies (Dict): Raw number of occurrences for each of the tokens

    Returns:
    dict: A dictionary with tokens and corresponding term frequency score

    In case of corrupt input arguments, None is returned
    """

    if not (isinstance(frequencies, dict) and frequencies
            and all(isinstance(word, str) for word in frequencies.keys())
            and all(isinstance(freq, int) for freq in frequencies.values())):
        return None
    tf_dict = {}
    number_of_occurrences = sum(frequencies.values())
    for word, quantity in frequencies.items():
        if not isinstance(word, str) and not isinstance(quantity, int):
            return None
        tf_dict[word] = quantity / number_of_occurrences
    print(tf_dict)
    return tf_dict


def calculate_tfidf(term_freq: dict[str, float], idf: dict[str, float]) -> Optional[dict[str, float]]:
    """
    Calculates TF-IDF score for each of the tokens
    based on its TF and IDF scores

    Parameters:
    term_freq (Dict): A dictionary with tokens and its corresponding TF values
    idf (Dict): A dictionary with tokens and its corresponding IDF values

    Returns:
    Dict: A dictionary with tokens and its corresponding TF-IDF values

    In case of corrupt input arguments, None is returned
    """
    if not (isinstance(term_freq, dict) and term_freq
            and isinstance(idf, dict) and all(isinstance(word, str) for word in idf.keys())
            and all(isinstance(word, str) for word in term_freq.keys())
            and all(isinstance(t_f, float) for t_f in term_freq.values())
            and all(isinstance(idf_value, float) for idf_value in idf.values())):
        return None
    tf_idf = {}
    for word in term_freq:
        if word not in idf.keys():
                idf[word] = log(47 / (0 + 1))
        tf_idf[word] = term_freq[word] * idf[word]
    print(tf_idf)
    return tf_idf


def calculate_expected_frequency(
        doc_freqs: dict[str, int], corpus_freqs: dict[str, int]
) -> Optional[dict[str, float]]:
    """
    Calculates expected frequency for each of the tokens based on its
    Term Frequency score for both target document and general corpus

    Parameters:
    doc_freqs (Dict): A dictionary with tokens and its corresponding number of occurrences in document
    corpus_freqs (Dict): A dictionary with tokens and its corresponding number of occurrences in corpus

    Returns:
    Dict: A dictionary with tokens and its corresponding expected frequency

    In case of corrupt input arguments, None is returned
    """
    pass


def calculate_chi_values(expected: dict[str, float], observed: dict[str, int]) -> Optional[dict[str, float]]:
    """
    Calculates chi-squared value for the tokens
    based on their expected and observed frequency rates

    Parameters:
    expected (Dict): A dictionary with tokens and
    its corresponding expected frequency
    observed (Dict): A dictionary with tokens and
    its corresponding observed frequency

    Returns:
    Dict: A dictionary with tokens and its corresponding chi-squared value

    In case of corrupt input arguments, None is returned
    """
    pass


def extract_significant_words(chi_values: dict[str, float], alpha: float) -> Optional[dict[str, float]]:
    """
    Select those tokens from the token sequence that
    have a chi-squared value smaller than the criterion

    Parameters:
    chi_values (Dict): A dictionary with tokens and
    its corresponding chi-squared value
    alpha (float): Level of significance that controls critical value of chi-squared metric

    Returns:
    Dict: A dictionary with significant tokens
    and its corresponding chi-squared value

    In case of corrupt input arguments, None is returned
    """
    pass
