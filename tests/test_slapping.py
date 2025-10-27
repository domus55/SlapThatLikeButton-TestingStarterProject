import pytest
from slapping.slap_that_like_button import slap_many, LikeState


def test_empty_slap():
    assert slap_many(LikeState.empty, '') is LikeState.empty


def test_single_slaps():
    assert slap_many(LikeState.empty, 'l') is LikeState.liked
    assert slap_many(LikeState.empty, 'd') is LikeState.disliked


@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ld', LikeState.disliked),
    ('dl', LikeState.liked),
    ('ldd', LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl', LikeState.liked),
])
def test_multi_slaps(test_input, expected):
    assert slap_many(LikeState.empty, test_input) is expected


def test_slaps():
    assert slap_many(LikeState.empty, '') is LikeState.empty
    assert slap_many(LikeState.empty, 'l') is LikeState.liked
    assert slap_many(LikeState.empty, 'd') is LikeState.disliked
    assert slap_many(LikeState.empty, 'll') is LikeState.empty
    assert slap_many(LikeState.empty, 'dd') is LikeState.empty
    assert slap_many(LikeState.empty, 'ld') is LikeState.disliked
    assert slap_many(LikeState.empty, 'dl') is LikeState.liked
    assert slap_many(LikeState.empty, 'ldd') is LikeState.empty
    assert slap_many(LikeState.empty, 'lldd') is LikeState.empty
    assert slap_many(LikeState.empty, 'ddl') is LikeState.liked
