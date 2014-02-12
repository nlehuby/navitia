#pragma once
#include "type/type.h"
#include "routing/routing.h"
#include "get_stop_times.h"
#include "type/pb_converter.h"

namespace navitia { namespace timetables {

typedef std::vector<std::string> vector_string;
typedef std::pair<DateTime, const type::StopTime*> vector_date_time;

pbnavitia::Response route_schedule(const std::string & line_externalcode,
        const std::vector<std::string>& forbidden_uris,
        const std::string &str_dt, uint32_t duration, uint32_t interface_version,
        const uint32_t max_depth, int count, int start_page, type::Data &d, bool disruption_active);

}}
