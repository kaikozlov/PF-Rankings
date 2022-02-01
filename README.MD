## PF Rankings

These rankings include all national bid tournaments hosted on [Tabroom](https://www.tabroom.com/index/index.mhtml) and make use of an elo-based system. Defeating a highly ranked team allows you to take a large number of points from them; defeating a lower ranked team gives you fewer from them. This article will involve a brief look into their methodology, but a later article will have more details.

The program and ranking methodology were originally created by [Inko Bovenzi](https://www.linkedin.com/in/inko-bovenzi-1997b01b4), but adapted by me in this repo.

### General Methodology

*   For every round in a tournament, the rankings look up both teams. If a team has debated before, we use their most recent elo. If they haven’t, they are assigned an elo of 1500.
*   The rankings compute a win probability that the outcome of the round occurs. For example, if a very strong team were debating a less-experienced team, and an upset occurred, the probability, p would be fairly low.
*   The winning team gains points in proportion to (1-p) and the strength of the tournament, estimated based on the number of bids.

In outrounds, there are three changes to the above:

1.  All elo point deductions are halved. This is to avoid penalizing teams that break, an important accomplishment, but then drop in earlier outrounds.
2.  The elo shift is weighted by the decision. A 3-0 is more decisive than a 2-1, a 4-1 more decisive than a 3-2.
3.  The winning team receives a flat elo bonus equal to the number of bids at the tournament divided by 2. For example, winning an outround at an octos bid would yield an 8-point bonus.

For more info, visit `METHODOLOGY.md`

### More Details about the Rankings

The rankings will be updated every week (or two weeks) depending on the tournament schedule in the week following the most recent tournaments. There may be changes to the methodology throughout the season once there is enough data for me to test the statistical efficacy of the rankings by looking at their Brier Scores. For example, I am considering changing the weighting of the tournaments based on their bid-level. Right now, rounds at an octos bid count twice as much as those as a quarters bid, and so on. This weighting feels a bit on the strong side.

The rankings were based on [FiveThirtyEight’s modified elo system](https://projects.fivethirtyeight.com/2021-nfl-predictions/?ex_cid=rrpromo) used for their football rankings and predictions.

### FAQ

#### Why are you doing rankings?

We think that rankings provide a valuable service to debaters across the country to see how they stack up against the competition nationally, in their state, and related to them in other ways. Without rankings, it’s difficult for a team from California to compare themselves to a New York team given that they’ll rarely encounter each other in rounds. Rankings are also fun!

#### What about previous seasons? Are my results from last year included in the calculus?

We think it's more interesting to have the season start with a blank slate and, pragmatically, it's very messy to track year after year do to school/partner switches and an ever increasing data set.

#### Why are there only Tabroom tournaments in the rankings? Can you include JoT or Speechwire?

Unfortunately, we cannot include non-Tabroom tournaments. The other tournament hosting websites do not provide their round-by-round data in a scrapable fashion.

#### Are you concerned about rankings lacking diversity?

Debate has a lot of inequities built into it, and sadly no ranking system will do anything to fix that. The rankings do not (of course) discriminate based on any demographics. The fact that the top teams are not always as diverse as we would wish is an indicator of the inequities in debate and a call to action to address them. Beyond that, We think that the rankings have the potential to improve the outlook ever so slightly for a couple reasons. First, debaters from under-represented demographics will be able to draw more attention to their accomplishments by using the universal nature of the rankings to compare themselves within that demographic, especially on things like college applications. Second, the rankings constitute irrefutable evidence of the inequities in debate and only further mandate solutions to these problems.

#### Are you concerned about rankings promoting elitism?

It's certainly a real concern, but it's not one that should incur the consequence of no rankings. First, in a competitive activity, there will inevitably be some who are better/worse at the game. To mask that is not productive when taking into account additional benefits. Second, rankings existing in and of themselves do not validate or justify inappropriate behavior. We aren't sold that they are a causal reason why some students abuse their perceived status.

#### Which other articles will you be publishing?

In the coming weeks, there will be deeper dives into the methodology of the rankings, as well as other interesting projects. Please check back regularly to see new articles!

#### How are these rankings different from other existing systems?

This is the only elo-based ranking system that currently exist in the debate space. We chose an elo system for its many advantages over other similar systems. For one, elo systems allow for easy comparison of the strength of teams around the country, irrespective of their frequency of competition or the size of the tournaments they attend. Unless you’re aiming for the top ten, once your elo stabilizes, attending more tournaments will not improve your ranking unless you meaningfully improve. This helps avoid biasing the rankings against top teams.

But for top teams, this changes. Due to the bonus points we give for winning outrounds, in order to maintain a top spot in the rankings, it is necessary to compete relatively frequency to avoid being overtaken. This is important to avoid one team dominating at a few tournaments early on and then holding the top spot for the rest of the season even if they stop debating or their performance declines. The rankings are dynamic at the top and quickly responsive to change thoroughout, but for most teams, there is no advantage to more frequent competition.