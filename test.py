"""test"""


def algo(rankings):
    """lol"""
    print rankings
    for cnt in range(0, len(rankings)/2):
        rankings[cnt] = (rankings[cnt]
                         if rankings[cnt] > rankings[cnt+1]
                         else rankings[cnt+1])
        rankings.pop(cnt+1)
    print rankings
TEST_DATA = [x for x in range(20)]
algo(TEST_DATA)
algo(TEST_DATA)
algo(TEST_DATA)
algo(TEST_DATA)
