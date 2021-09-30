select managers.name
from managers, teams
where managers.team_id = teams.team_id and teams.name = 'All Stars'
;