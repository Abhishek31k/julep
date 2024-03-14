from uuid import UUID

from ...autogen.openapi_model import FunctionDef


def update_tool_by_id_query(
    agent_id: UUID, tool_id: UUID, function: FunctionDef, embedding: list[list[float]]
) -> str:
    # Agent update query
    agent_id = str(agent_id)
    tool_id = str(tool_id)
    function = function.model_dump()

    name = function["name"]
    description = function["description"]
    # parameters = ParametersDict(**function["parameters"]).model_dump(exclude_none=True)
    parameters = function.get("parameters", {})

    return f"""
        ?[agent_id, tool_id, name, description, parameters, embedding, updated_at] <- [
            [to_uuid("{agent_id}"), to_uuid("{tool_id}"), "{name}", "{description}", {parameters}, vec({embedding}), now()]
        ]

        :update agent_functions {{
            agent_id,
            tool_id,
            name,
            description,
            parameters,
            embedding,
            updated_at,
        }}
        :returning
    """
