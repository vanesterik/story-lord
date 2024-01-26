from typing import Dict, List, Literal

from openai.types.chat import ChatCompletionMessageParam

PropmpType = Literal["academic", "normal", "story"]


prompt_messages: Dict[PropmpType, List[ChatCompletionMessageParam]] = {
    "academic": [
        {
            "role": "system",
            "content": """
When I ask for help to write something, you will reply in the academic formal style.
""",
        }
    ],
    "normal": [],
    "story": [
        {
            "role": "system",
            "content": """
Answer in markdown format with description, functional notes, acceptance criteria and test notes as paragraphs.
Description paragraph should not have a title. Wrap all mentions of components in backticks.
Place all code snippets in code blocks.
""",
        },
        {
            "role": "user",
            "content": """
You are a business analyst. Write a user story on developing a `ReviewBarChart` subcomponent.
""",
        },
        {
            "role": "assistant",
            "content": """
# Develop `ReviewBarChart` subcomponent

As a business analyst, I would like a `ReviewBarChart` subcomponent to be developed that will be integrated as a key part of the `ProductReviews` organisms component. This `ProductReview` component should enable the effective display and interaction with product ratings within the `ProductReviews` section.

## Functional Notes

- Add `ReviewBarChart` subcomponent to the components folder of `ProductReviews` organism component
- Create an empty Storybook story to mock and develop this organism component.
- Follow the latest design: [insert design link here]
- Use Storybook controls to interact with component.

## Acceptance Criteria

- The `ReviewBarChart` subcomponent has been successfully developed, meeting the specified functional requirements.
- The `ReviewBarChart` subcomponent is able to be seamlessly integrated within the `ProductReviews` organisms component.
- The `ReviewBarChart` component effectively displays and updates product ratings based on Storybook controls.

## Test Notes

- Conduct testing in Storybook environment to verify that the `ReviewBarChart` subcomponent functions as intended.
- Validate that the `ReviewBarChart` subcomponent meets the design and functional requirements set for it within the `ProductReviews` context.
""",
        },
    ],
}


class Prompt:
    def __init__(self, type: PropmpType = "story") -> None:
        self._type = type

    @property
    def type(self) -> str:
        return self._type

    def parse_prompt_messages(self, query: str) -> List[ChatCompletionMessageParam]:
        messages = prompt_messages[self._type]
        messages.append(
            {
                "role": "user",
                "content": query,
            }
        )
        return messages

    def enable_prompt_type(self, type: PropmpType) -> None:
        self._type = type
