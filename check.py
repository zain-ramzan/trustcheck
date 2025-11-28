from translate import translate_text, get_generator
import difflib
import json

def round_trip_similarity(original_nl, gen):
    intent_str = translate_text(original_nl, gen=gen)
    back_prompt = f"Convert this intent JSON to a short natural language sentence:\n{intent_str}\n"
    back = gen(back_prompt, max_length=128, do_sample=False)[0].get("generated_text","")
    s = difflib.SequenceMatcher(None, original_nl.lower(), back.lower())
    return s.ratio(), intent_str, back

def sanity_checks(parsed_json):
    issues = []
    if "action" not in parsed_json:
        issues.append("Missing action")
    if "source" not in parsed_json or "destination" not in parsed_json:
        issues.append("Missing endpoints")
    return issues
