import sys

from fabric.api import run, env, cd, prefix, task


@task
def prod():
    env.prefix = 'source /home/webmaster/.virtualenvs/pangolin/bin/activate'
    env.user = 'webmaster'
    env.hosts = ['pangolin.com']
    env.path = '/home/webmaster/apps/pangolin'
    env.branch = 'master'
    env.db_name = 'pangolin'
    env.app = 'pangolin'


@task
def test():
    env.prefix = 'source /home/webmaster/.virtualenvs/pangolin/bin/activate'
    env.user = 'webmaster'
    env.hosts = ['test.pangolin.com']
    env.path = '/home/webmaster/apps/pangolin'
    env.branch = 'master'
    env.db_name = 'pangolin'
    env.app = 'pangolin'


if 'prod' not in sys.argv:
    test()


@task
def manage(command):
    with cd(env.path), prefix(env.prefix):
        run('python manage.py {0}'.format(command))


@task
def update():
    pull()
    clean()
    requirements()
    collectstatic()
    # compilemessages()
    migrate()
    restart()


@task
def pull():
    with cd(env.path):
        run('git pull origin {0}'.format(env.branch))


@task
def clean():
    with cd(env.path):
        run('find . -name "*.pyc" -exec rm -f {} \;')


@task
def requirements():
    with cd(env.path), prefix(env.prefix):
        run('pip install -r requirements.txt')


@task
def db():
    stop()
    dropdb()
    createdb()
    migrate()
    loaddata()
    start()


@task
def dropdb():
    run('dropdb {0}'.format(env.db_name))


@task
def createdb():
    run('createdb {0}'.format(env.db_name))


@task
def migrate():
    manage('migrate')


@task
def loaddata():
    manage('filldb')


@task
def collectstatic():
    manage('collectstatic --noinput')


@task
def compilemessages():
    manage('compilemessages')


@task
def restart():
    run('supervisorctl restart {0}:'.format(env.app))


@task
def start():
    run('supervisorctl start {0}:'.format(env.app))


@task
def stop():
    run('supervisorctl stop {0}:'.format(env.app))


@task
def status():
    run('supervisorctl status')
