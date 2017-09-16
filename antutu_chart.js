function get_chart_data() {
	
	var rank_chart = document.getElementsByClassName('rank_tb')[0].tBodies;
	var chart_lines = rank_chart[0].childNodes;
	var chart_data = Array();

	for ( var lineno = 0 ; lineno < chart_lines.length ; lineno ++ ) {
		if ( chart_lines[lineno].childNodes.length > 0 ) {
			var chart_line = chart_lines[lineno].getElementsByTagName('td');
			if ( chart_line.length == 5 ) {
				
				var line_data = {
					'model':chart_line[0].getElementsByClassName('rank_left')[0].textContent,
					'cpu_rate': chart_line[1].textContent,
					'ux_rate': chart_line[2].textContent,
					'3d_rate': chart_line[3].textContent,
					'total_rate': chart_line[4].textContent
				};
				chart_data[chart_data.length] = line_data;
			
			}
		}
	}

	return chart_data;

}
