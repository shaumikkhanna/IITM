select name
from players
where team_id = (select team_id from teams where name = 'All Stars')
;
