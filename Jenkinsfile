pipeline {
    agent any  // Использовать любой доступный агент для выполнения

    environment {
        DOCKER_IMAGE = 'my_app_image'  // Имя для вашего Docker-образа
        DOCKER_CONTAINER = 'my_app_container'  // Имя для вашего Docker-контейнера
        LOGIN = credentials('LOGIN')
    }

    stages {
        stage('Build Docker Image') {
                steps {
                    script {
                        // Сборка Docker-образа
                        sh '''
                        docker build -t ${DOCKER_IMAGE} .
                        '''
                    }
                }
            }
        stage('print env') {
            steps {
                script{
                sh ''' echo ${LOGIN} '''
                }
            }
        }

        stage('Run Docker Container') {
                steps {
                    script {
                        // Запуск Docker-контейнера
                        sh '''
                        docker run --name ${DOCKER_CONTAINER} -d ${DOCKER_IMAGE}  # Замените на вашу команду запуска, если необходимо
                        '''
                    }
                }
            }

        stage('Run Tests') {  // Стадия для запуска тестов
            steps {
                script {
                    sh 'docker exec ${DOCKER_CONTAINER} browserstack-sdk pytest /test/test_habit.py:TestStartPage:test_click_skip_onboarding' // Запустите тесты внутри контейнера
                }
            }
        }

        stage('Stop and Remove Container') {
                steps {
                    script {
                        // Остановка и удаление контейнера
                        sh '''
                        docker stop ${DOCKER_CONTAINER} || true  # Остановка контейнера (если он еще работает)
                        docker rm ${DOCKER_CONTAINER} || true    # Удаление контейнера
                        '''
                    }
                }
            }
    }
    post {
        always {
            echo 'Final cleanup in post section...'
            // В данном случае мы также можем делать финальную очистку
            sh 'docker stop ${DOCKER_CONTAINER} || true'
            sh 'docker rm ${DOCKER_CONTAINER} || true'
        }
    }
}
