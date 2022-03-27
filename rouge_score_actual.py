from rouge import Rouge

bart = "Time Warner profits up 76% to $1.13bn in 4th quarter. Firm one of Google's biggest investors But AOL " \
        "loses 464,000 subscribers to Time Warner. Firm set to restate AOL results after SEC probe. 'Strong' " \
        "results 'enhance flexibility' for Time Warner "

t5 = "quarter profits at US media giant TimeWarner jumped 76% to $1.13bn (£600m) for the three months to " \
      "December. it benefited from sales of high-speed internet connections and higher advert sales, " \
      "according to a report by the US Securities Exchange Commission (SEC) it lost 464,000 subscribers in " \
      "the fourth quarter profit was lower than in preceding three quarters, but its own internet business, " \
      "AOL, had mixed fortunes. "

pegasus = "Time Warner, owner of Warner Bros and AOL, has reported a sharp rise in fourth quarter profits."

reference = "Quarterly profits at US media giant TimeWarner jumped 76% to $1.13bn due to sales of high-speed internet " \
            "connections and higher advert sales. It now owns 8% of search engine Google. AOL lost 464," \
            "000 subscribers in the fourth quarter. TimeWarner is to restate its accounts as part of efforts to " \
            "resolve an inquiry into AOL by US market regulators. It has already offered to pay $300m to settle " \
            "charges, in a deal that is under review by the SEC. "

rouge04 = Rouge()
scores_bart = rouge04.get_scores(bart, reference)
print(scores_bart)
print()
scores_t5 = rouge04.get_scores(t5, reference)
print(scores_t5)
print()
scores_pegasus = rouge04.get_scores(pegasus, reference)
print(scores_pegasus)
print()