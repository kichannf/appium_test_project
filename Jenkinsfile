pipeline {
    agent any  // Использовать любой доступный агент для выполнения

    environment {
        DOCKER_IMAGE = 'my_app_image'  // Имя для вашего Docker-образа
        DOCKER_CONTAINER = 'my_app_container'  // Имя для вашего Docker-контейнера
    }

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

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Здесь ваши команды для развёртывания приложения
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}