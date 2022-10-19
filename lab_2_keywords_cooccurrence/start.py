"""
Co-occurrence-driven keyword extraction starter
"""

from pathlib import Path
from lab_2_keywords_cooccurrence.main import (extract_phrases,
                                              extract_candidate_keyword_phrases,
                                              calculate_frequencies_for_content_words,
                                              calculate_word_degrees,
                                              calculate_word_scores,
                                              calculate_cumulative_score_for_candidates,
                                              get_top_n,
                                              extract_candidate_keyword_phrases_with_adjoining,
                                              calculate_cumulative_score_for_candidates_with_stop_words)


def read_target_text(file_path: Path) -> str:
    """
    Utility functions that reads the text content from the file
    :param file_path: the path to the file
    :return: the text content of the file
    """
    with open(file_path, 'r', encoding='utf-8') as target_text_file:
        return target_text_file.read()


if __name__ == "__main__":
    # finding paths to the necessary utils
    PROJECT_ROOT = Path(__file__).parent
    ASSETS_PATH = PROJECT_ROOT / 'assets'

    # reading list of stop words
    STOP_WORDS_PATH = ASSETS_PATH / 'stop_words.txt'
    with open(STOP_WORDS_PATH, 'r', encoding='utf-8') as fd:
        stop_words = fd.read().split('\n')

    # reading the text from which keywords are going to be extracted
    TARGET_TEXT_PATH_GENOME = ASSETS_PATH / 'genome_engineering.txt'
    TARGET_TEXT_PATH_ALBATROSS = ASSETS_PATH / 'albatross.txt'
    TARGET_TEXT_PATH_PAIN_DETECTION = ASSETS_PATH / 'pain_detection.txt'
    TARGET_TEXT_PATH_GAGARIN = ASSETS_PATH / 'gagarin.txt'

    corpus = {
        'gagarin': read_target_text(TARGET_TEXT_PATH_GAGARIN),
        'albatross': read_target_text(TARGET_TEXT_PATH_ALBATROSS),
        'genome_engineering': read_target_text(TARGET_TEXT_PATH_GENOME),
        'pain_detection': read_target_text(TARGET_TEXT_PATH_PAIN_DETECTION)
    }

    CANDIDATE_PHRASES = None
    FREQUENCIES = None
    DEGREES = None
    SCORES = None
    CUMULATIVE_SCORE_FOR_CANDIDATES = None
    WITH_ADJOINING = None
    CUMULATIVE_SCORE_STOP_WORDS = None
    EXTRACTION = extract_phrases(corpus['gagarin'])

    if EXTRACTION:
        CANDIDATE_PHRASES = extract_candidate_keyword_phrases(EXTRACTION, stop_words)

    if CANDIDATE_PHRASES:
        FREQUENCIES = calculate_frequencies_for_content_words(CANDIDATE_PHRASES)

    if FREQUENCIES:
        DEGREES = calculate_word_degrees(CANDIDATE_PHRASES, list(FREQUENCIES.keys()))

    if DEGREES:
        SCORES = calculate_word_scores(DEGREES, FREQUENCIES)

    if SCORES:
        CUMULATIVE_SCORE_FOR_CANDIDATES = calculate_cumulative_score_for_candidates(CANDIDATE_PHRASES, SCORES)

    if CUMULATIVE_SCORE_FOR_CANDIDATES:
        print(f'Top candidates by cumulative score: {get_top_n(CUMULATIVE_SCORE_FOR_CANDIDATES, 5, 2)}')

    if CANDIDATE_PHRASES and EXTRACTION:
        WITH_ADJOINING = extract_candidate_keyword_phrases_with_adjoining(CANDIDATE_PHRASES, EXTRACTION)

    if WITH_ADJOINING:
        CUMULATIVE_SCORE_STOP_WORDS = calculate_cumulative_score_for_candidates_with_stop_words(WITH_ADJOINING, SCORES,
                                                                                                stop_words)

    RESULT = WITH_ADJOINING
    assert RESULT, 'Keywords are not extracted'
