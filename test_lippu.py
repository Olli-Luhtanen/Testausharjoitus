"""Testit lippu.py-moduulille. Täydennä tehtävien mukaan (ks. README.md)."""

import pytest

from lippu import kokonaishinta, lippuhinta


def test_aikuisen_hinta():
    # Arrange: valmistellaan syöte
    ika = 30
    # Act: kutsutaan testattavaa funktiota
    hinta = lippuhinta(ika)
    # Assert: tarkistetaan tulos
    assert hinta == 15.0


# TEHTÄVÄ 2: Raja-arvot yhdellä parametrisoidulla testillä.
# Täydennä alla olevaan listaan pareja (ikä, odotettu hinta).
# Poista sen jälkeen rivi @pytest.mark.skip.
@pytest.mark.parametrize(
    "ika, odotettu, Opiskelija",
    [
        (0, 0.0, False),
        (6, 0.0, False),
        (7, 8.0, False),
        (17, 8.0, False),
        (18, 15.0, False),
        (65, 10.0, False),
        (17, 8.0, True),
        (18, 10.0, True),
        (64, 10.0, True),
        (65, 10.0, True)
    ],
)

def test_lippuhinta_raja_arvot(ika, odotettu, Opiskelija):
    assert lippuhinta(ika,Opiskelija) == odotettu


# TEHTÄVÄ 3: Virheelliset iät nostavat ValueErrorin.
# Vinkki: with pytest.raises(ValueError):
def test_virheelliset_iat():
    with pytest.raises(ValueError):
        lippuhinta(-1)
    with pytest.raises(ValueError):
        lippuhinta(121)

# TEHTÄVÄ 4: Kokonaishinta ja ryhmäalennuksen raja (9 ja 10 lippua).

def test_kokonaishinta():
    assert kokonaishinta([]) == 0.0

    iat_9 = [30] * 9 
    assert kokonaishinta(iat_9) == 135.0

    iat_10 = [30] * 10 
    assert kokonaishinta(iat_10) == 150.0 * (1 - 0.10)
