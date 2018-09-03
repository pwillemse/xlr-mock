from xlrelease.reader.json.Reader import Reader
from xlrelease.Release import Release


template = Reader.read_from_file('examples/example-1.json')
release = Release(template)

vars = {
    'DAR_PRESENT': 'TRUE',
    'ENABLE_DEPLOY': 'FALSE',
    'VERSION': '1.2.3',
    'ENABLE_DEPLOY_ET_PR': 'TRUE'
}

release.find_task('Load Application Variables').return_variables(vars)

release.execute()
for phase in release.get_phases():
    print 'Phase: %s, are tasks executed: %s' % (phase.get_title(), phase.are_tasks_executed())
