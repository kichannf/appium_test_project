pipeline {
    agent any  // Использовать любой доступный агент для выполнения

    environment {
        DOCKER_IMAGE = 'my_app_image'  // Имя для вашего Docker-образа
        DOCKER_CONTAINER = 'my_app_container'  // Имя для вашего Docker-контейнера
    }

    stages {
        stage('Build Docker Image') {
                steps {
                    script {
                        // Сборка Docker-образа
                        sh '''
                        docker build -t ${DOCKER_IMAGE}  .
                        '''
                    }
                }
            }
        stage('Print env') {
            steps {
                script{
                sh ''' echo "${LOGIN}" '''
                }
            }
        }

        stage('Run Docker Container') {
                steps {
                    script {
                        // Запуск Docker-контейнера
                        sh '''
                        docker run --name ${DOCKER_CONTAINER} -d ${DOCKER_IMAGE}  # Замените на вашу команду запуска, если необходимо

                        docker exec ${DOCKER_CONTAINER} sh -c "
                        touch .env && chmod 666 .env &&
                        echo 'BROWSERSTACK_USERNAME=${BROWSERSTACK_USERNAME}' >> .env &&
                        echo 'BROWSERSTACK_ACCESS_KEY=${BROWSERSTACK_ACCESS_KEY}' >> .env &&
                        echo 'LOGIN=${LOGIN}' >> .env &&
                        echo 'PASSWORD=${PASSWORD}' >> .env &&
                        cat .env && cat browserstack.yml"
                        '''
                    }
                }
            }

        stage('Run Tests') {  // Стадия для запуска тестов
            steps {
                script {
                    sh ''' docker exec ${DOCKER_CONTAINER} browserstack-sdk pytest ./test/test_habit.py:TestStartPage:test_click_skip_onboarding''' // Запустите тесты внутри контейнера
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
//     post {
//         failure {
//             echo 'Final cleanup in post section...'
//             // В данном случае мы также можем делать финальную очистку
//             sh 'docker stop ${DOCKER_CONTAINER} || true'
//             sh 'docker rm ${DOCKER_CONTAINER} || true'
//         }
//     }
}
