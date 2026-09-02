---
title: AC Guidelines
layout: default
weight: 6
hide: false
---

> **Stub starting point.** Copied from AISTATS 2025 and lightly generalised. Fold in process changes each year, then copy improvements back into this stub.

# {{ site.conference.short_name }} {{ site.conference.year }} AC Guidelines

This page provides guidelines for Area Chairs (ACs) for {{ site.conference.short_name }} {{ site.conference.year }}. It is seeded from recent AISTATS conferences (and earlier NeurIPS AC guidance); update process details before publishing.

## Responsibilities of an Area Chair (AC)

  1. Identify desk-rejection cases (e.g., papers with unacceptable formatting issues, dual submissions; see [FAQ below](#frequently-asked-questions))
  2. Help reviewer assignments by recruiting expert reviewers and adjusting reviewer assignments
  3. Monitor the review process and ensure reviewers are responsive
  4. Ensure the submissions have high-quality reviewers
  5. Organize reviewer discussions after author feedback
  6. Make acceptance/rejection recommendations based on reviews, author feedback, discussions, and their own understanding of the submission
  7. Recommend accepted submissions for oral talks
  8. Resolve any issue during the review process, e.g., by recruiting emergency reviewers, addressing concerns from both reviewers and authors, and/or raising concerns with Senior ACs and Program Chairs.

## Important Dates

{% include listdates.html %}

## Main Tasks

Below is a list of tasks (and the detailed explanations) that an AC is expected to conduct.

1. Registrations on OpenReview

   -  Make sure your profile on OpenReview is up-to-date. Adding your conflict of interests as well as selecting your expertise topics. Import papers to your OpenReview profile.
   - Read and agree to abide by the [{{ site.conference.short_name }} code of conduct]({{ "code-of-conduct.html" | relative_url }}).

2. Paper bidding

    - We will assign papers to ACs and reviewers using a combination of bids and a matching algorithm supported by the TPMS paper matching system.
    - After receiving the initial assignment, quickly check the submissions and identify desk-reject and/or conflict-of-interest cases if applicable.
    - It is possible that some of the submissions in your batch might not be closely related to your expertise. As we have a large number of submissions, your flexibility is greatly appreciated. When making decisions in later stages, contact Senior AC if you need help for the submissions that are too far away from your expertise area

3. Reviewer assignments adjustments

    - Make sure that every submission in your batch is matched with 5 suitable reviewers whom you can trust on this submission, ideally with a diverse set of opinions.
    - Do invest time for this before the reviewing process starts to ensure that your batch has expert reviewers - this will make your life much easier in reducing the number of borderline and mis-judged cases.

4. Monitor the review process and ensure reviewers are responsive

    - Send reminders to reviewers for submitting reviews on time.
    - Recruit emergency reviewers if not having enough high-quality reviews, or having reviews with diverging opinions, 1 week before the review release date.
    - Ask reviewers to rewrite and resubmit their review if appropriate.
    - Please ensure reviewers provide their comments with evidence. E.g., if a reviewer selects “combinatorial approach” in their answer to the question regarding novelty, ensure that in the next question that reviewer has provided the corresponding references to justify this choice.

5. Author-Reviewer discussion

    - Ensure that reviewers engage in discussions with the authors during this period.
    - It is highly recommended that they at least acknowledge that they have read the comments and indicate any change in their scores (or lack thereof).
    - Encourage them to discuss with other reviewers.

6. Reviewer-AC discussion

    - Initiate and lead discussions between reviewers. At this point you should read both reviews and author feedback, to understand the pros and cons of the submission, as well as the major disagreements between reviewers and authors. List these points in your discussion post. If applicable, explicitly ask reviewers with e.g., very high/low scores to explain their opinions.
    - Read confidential messages from reviewers and authors. If applicable, contact the corresponding reviewers to address authors’ concerns (without revealing the authors’ confidential comments).

7. Decision making and meta-review

    - Be on time in writing your meta-review and making decisions – we have a tight schedule regarding final decisions!
    - You should write the meta reviews based on your reading of the paper, the reviews, the author feedback, and the reviewer discussions. Keep in mind that the meta-review needs to provide a convincing justification about your decision (especially in rejection cases).
    - The meta-review should augment the reviews, and explain how the reviews, the author response, and the discussions were used to arrive at your recommendation. Do not dismiss or ignore a review or author feedback unless you have a good reason for doing so; in such case you should also explain this in your meta review.
    - If uncertain about your decision, reach out to your SAC as early as you can. For papers where the reviewers cannot come to a consensus, you should read the paper carefully and write a detailed meta-review. You are expected to discuss such difficult cases with your SAC.
    - For submissions with rejection decisions, you are encouraged to also provide comments regarding potential ways to improve the paper.

## Best Practices

  - Please respect deadlines and respond to emails as promptly as possible.
  - It is okay to be unavailable for part of the review process (e.g., on vacation for a few days). Contact SAC if you will be unavailable for more than that—especially during important windows such as the last week of reviewing and/or meta review.
  - Be professional and listen to both reviewers and authors. However, your responsibility is not just to facilitate reviewer discussions and calculate average scores. We expect you to be familiar with all the submissions in your batch and to be able to justify your meta review with technical arguments.
  - Be kind and considerate: personal situations may lead to late or unfinished work among reviewers. In the event that a reviewer is unable to complete their work on time, you might have to find emergency reviewers or even provide your own review. In all communications, exhibit empathy and understanding.
  - If you notice unethical or suspicious behavior involving either authors or reviewers, please notify your SAC and the Program Chairs.

## Writing the meta-review

_Adapted from NeurIPS 2025 AC guidelines. Original source: Chris Williams and John Lafferty._

  - Don't focus too much on the scores. Instead, look carefully at the comments.
  - Judge the quality of the review rather than taking note of the reviewer's confidence score; the latter may be more a measure of personality.
  - Compare the reviewers’ answers regarding their provided keywords for the submission and their expertise. Also compare it with the keywords specified by the authors. A mismatch between these keywords may indicate clarity issues and/or misunderstandings.
  - Indicate that you have read the author feedback and explicitly write about whether the rebuttal has addressed (some of) the reviewers’ concerns or not.
  - If you use information that is not in the reviews (e.g., new arguments in reviewer-AC discussions), tell the authors (a) that you have done so and (b) what that information is.
  - If you find yourself wanting to overrule a unanimous opinion of the reviewers, the standards for your summary should be at the level of a full review. In these cases, we also suggest soliciting an auxiliary review if possible.
  - Please attempt to take a decisive stand on borderline papers – we know these are tough decisions and we need your judgment here. Much of our work will involve borderline papers where no one confidently expresses excitement, nor are any major problems identified.
  - Try to counter biases you perceive in the reviews. Unfashionable subjects should be treated fairly but often aren't, to the advantage of the papers on more mainstream approaches. It is important to encourage risk and recognize that new approaches can't initially yield SOTA results. Nor are they always sold according to the recipes we are used to.

For more tips for area chairs of ML conferences, have a look at [this blog post](https://team-approx-bayes.github.io/blog/ACtips/).

## LLM Policy

The use of LLMs is not allowed to write papers, reviews, and meta-reviews. They can be used as an assist tool, for example, to check grammatical issues. Ultimately, you are responsible for the text you write, including content generated by LLMs that could be construed as plagiarism or scientific misconduct (e.g., fabrication of facts). Similar to other ML venues, at AISTATS too, LLMs are not eligible for authorship.

## Confidentiality

You must keep everything relating to the review process confidential. Do not use ideas, code and results from submissions in your own work until they become publicly available (e.g., via a technical report or a published paper for ideas/results, via open source for code, etc.). Do not talk about or distribute submissions (whether it is the code, or the ideas and results described in them) to anyone without prior approval from the program chairs. Code submitted for reviewing cannot be distributed. DO NOT talk to other ACs and/or SACs about submissions that are assigned to you unless you have a justified reason to do so, in such case before contacting other ACs/SACs, consult with your SAC and/or the Program Chairs.

## Frequently Asked Questions

1. How do I contact the Senior Area Chair (SAC) and/or the Program Chairs?

    OpenReview provides contacting functions to do so once you’ve been assigned to an SAC. Also, you can contact the Program Chairs{%if site.author.email %} via [{{ site.author.email }}](mailto:{{ site.author.email }}){%endif%}.
2. What if the paper does not have the reproducibility checklist?

    This does not count for desk-reject, although you should check whether the authors have submitted the checklist during author feedback. Remind the authors of accepted submissions to include the checklist in camera ready.
3. What is the page limit?

    In the review period, the main part of the submission should be 8 pages long. After that, only the references are allowed. If that is not the case, please mark it as a format violation.
4. What else counts as format violations?

    Anything that breaks anonymity, violates dual submission policy, changes the format (e.g., margins or vertical spaces). If in doubt, please mark it as a violation, which will be looked after by the Program Chairs.
