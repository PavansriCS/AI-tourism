from flask import Blueprint

from controllers.ai_controller import chat, history, recommendations, trip_plan

ai_bp = Blueprint("ai", __name__)
ai_bp.post("/recommendations")(recommendations)
ai_bp.post("/trip-plan")(trip_plan)
ai_bp.post("/chat")(chat)
ai_bp.get("/chat/history")(history)

