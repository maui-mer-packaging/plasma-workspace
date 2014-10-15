/*
    Copyright (C) 2014  Martin Klapetek <mklapetek@kde.org>

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
*/

#include "notificationshelperplugin.h"
#include "notificationshelper.h"

#include <QtQml>
#include <QUrl>

class UrlHelper : public QObject {
    Q_OBJECT
    public:
        Q_INVOKABLE bool isUrlValid(const QString &url) const {
           return QUrl::fromUserInput(url).isValid();
        }
};

static QObject *urlcheck_singletontype_provider(QQmlEngine *engine, QJSEngine *scriptEngine)
{
    Q_UNUSED(engine)
    Q_UNUSED(scriptEngine)

    return new UrlHelper();
}

void NotificationsHelperPlugin::registerTypes(const char *uri)
{
    Q_ASSERT(uri == QLatin1String("org.kde.plasma.private.notifications"));

    qmlRegisterType<NotificationsHelper>(uri, 1, 0, "NotificationsHelper");
    qmlRegisterSingletonType<UrlHelper>(uri, 1, 0, "UrlHelper", urlcheck_singletontype_provider);

}

#include "notificationshelperplugin.moc"