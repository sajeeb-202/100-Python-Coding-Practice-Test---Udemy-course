def merge_mails(template, data):

    if not data:
        return []

    result = []

    for entry in data:
        personalized_email = template

        for key, value in entry.items():
            placeholder = "{{" + key + "}}"
            personalized_email = personalized_email.replace(
                placeholder, str(value)
            )

        result.append(personalized_email)

    return result